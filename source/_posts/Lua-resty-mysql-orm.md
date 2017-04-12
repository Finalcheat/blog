title: lua-resty-mysql的简单封装
date: 2017/04/12 21:02:00
tags:
- openresty
- lua
- mysql
categories:
- openresty

---
## [lua-resty-mysql](https://github.com/openresty/lua-resty-mysql)
原生[lua-resty-mysql](https://github.com/openresty/lua-resty-mysql)的操作比较原始，这里将它的操作进行一个简单的封装。

### 思路
基本方法就是以lua的table作为参数，然后将table转成sql语句最后交给lua-resty-mysql执行。

### [Code](https://gist.github.com/Finalcheat/bd1a508a1ef1bd015357c1de350d3674)
```
local mysql = require "resty.mysql"

-- 数据库配置
local st = require "settings"

local _M = { _version = "0.1" }

local mt = { __index = _M }


function _M.new(self, o)
    o = o or { _database = st.mysql.database }
    setmetatable(o, mt)
    return o
end

-- 获取数据库连接
function _M.get_conn(self, conn_info)
    conn_info = conn_info or {}
    local db, err = mysql:new()
    if not db then
        ngx.log(ngx.ERR, "failed to instantiate mysql: " .. err)
        return nil
    end
    -- 默认超时3000ms
    local timeout = conn_info.timeout or 3000
    db:set_timeout(timeout)
    local mysql_st = st.mysql
    local database = conn_info.database or self._database
    local host = mysql_st.host
    local port = mysql_st.port
    local user = mysql_st.user
    local password = mysql_st.password
    local ok, err, errcode, sqlstate = db:connect{
        host = host,
        port = port,
        database = database,
        user = user,
        password = password,
    }
    if not ok then
        ngx.log(ngx.ERR, "failed to connect: " .. err .. ": " .. errcode .. " " .. sqlstate)
        return nil
    end
    if db:get_reused_times() == 0 then
        -- 第一次使用，设置编码utf8，避免获取到的中文数据出现乱码
        db:query("SET NAMES utf8")
    end
    return db
end


-- 插入封装
-- table_name: 数据库表
-- item: 插入的内容
function _M.insert(self, table_name, item)
    local fields_item = {}
    local values_item = {}
    local index = 1
    for field, value in pairs(item) do
        fields_item[index] = "`" .. field .. "`"
        values_item[index] = ngx.quote_sql_str(value)
        index = index + 1
    end
    local sql = string.format("INSERT INTO %s (%s) VALUES (%s)", table_name,
                              table.concat(fields_item, ","),
                              table.concat(values_item, ","))
    local db = self:get_conn()
    local res, err, errcode, sqlstate = db:query(sql)
    if not res then
        ngx.log(ngx.ERR, "bad result: " .. err .. ": " .. errcode .. ": " .. sqlstate)
        return nil, err, errcode, sqlstate
    end
    db:set_keepalive(10000, 100)
    return res
end


-- 查询封装
-- table_name: 数据库表
-- query_table: 查询内容
function _M.find(self, table_name, query_table)
    local columns = query_table.columns or "*"
    local conditions = query_table.conditions or ""
    local bind = query_table.bind or {}
    local order = query_table.order or ""
    local limit = tonumber(query_table.limit) or -1
    local offset = tonumber(query_table.offset) or -1

    for k, v in pairs(bind) do
        local regex = ":" .. k .. ":"
        conditions, n, err = ngx.re.sub(conditions, regex, ngx.quote_sql_str(v))
        if not conditions then
            ngx.log(ngx.ERR, err)
            return nil
        end
    end

    local sql = string.format("SELECT %s FROM %s", columns, table_name)

    if #conditions ~= 0 then
        sql = string.format("%s WHERE %s", sql, conditions)
    end

    if #order ~= 0 then
        sql = string.format("%s %s", sql, order)
    end

    if offset > 0 then
        sql = string.format("%s OFFSET %s", sql, offset)
    end

    if limit > 0 then
        sql = string.format("%s LIMIT %s", sql, limit)
    end

    local db = self:get_conn()
    local res, err, errcode, sqlstate = db:query(sql)
    if not res then
        ngx.log(ngx.ERR, "bad result: " .. err .. ": " .. errcode .. ": " .. sqlstate)
        return nil, err, errcode, sqlstate
    end
    db:set_keepalive(10000, 100)
    return res
end
```

### insert使用
```
-- require上面的代码
local ms = require "modules.mysql"

-- 数据库表名
local table_name = "users"

-- 插入的内容
local item = {
    username = "username1",
    salt = "salt1",
    password = "password1",
}

-- 构造
local mysql = ms:new()

-- 执行插入，内部就是将item转化为sql语句并执行返回，此处就是转化为INSERT INTO users (username, salt, password) VALUES ("username1", "salt1", "password1");
local result = mysql:insert(table_name, item)

-- 此处result原样返回结果，nil则为失败，否则返回插入的信息，例如insert_id等信息
if result then
    ngx.log(ngx.INFO, "insert id: " .. result.insert_id)
end
```

### find使用
```
-- require上面的代码
local ms = require "modules.mysql"

-- 数据库表名
local table_name = "users"

-- 需要查询的列，与原生sql一样，多列需要用逗号隔开
local columns = "uid"

-- 查询条件，:name:表示参数占位，将会由bind中的值替换
local conditions = "username = :username: AND salt = :salt: AND password = :password:"
local bind = {
    username = "username2",
    salt = "salt2",
    password = "password2",
}

-- 构造最终所有查询的条件，除了下面这些还有order和offset
local query_table = {
    columns = columns,               -- 查询的列(select与from之间的值)
    conditions = conditions,         -- 查询的条件(主要是where后面的值)
    bind = bind,                     -- 查询条件参数替换
    limit = 1,                       -- 限制返回条数(sql语句的limit)
}
   
-- 构造
local mysql = ms:new()

-- 指向查询，内部是将query_table转化为sql语句并执行返回，此处就是转化为SELECT uid FROM users WHERE username = "username2" AND salt = "salt2" AND password = "password2" LIMIT 1;
local result = mysql:find(table_name, query_table)

-- 此处result原样返回结果
if result and #result ~= 0 then
    ngx.log(ngx.INFO, "find uid: " .. result[1].uid)
end
```
