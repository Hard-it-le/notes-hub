1、判断 targetIds 是否为空，如果不为空，则添加到查询条件 query 中

2、查询当前用户池中是否有 hidden ，如果有,则查询条件中过滤掉

3、根据用户池 id 和 system 查询对应用户池的系统权限空间

4、判断 namespaceCodeList 是否为空
- 为空，过滤系统权限空间
- 不为空并且包含 system，query 设置 namespace  的查询条件，查询 policies 表的默认策略并过滤掉 code 为 AuthingUserPoolSensitiveAccess 和 AdministratorAccess 策略,如果默认策略不为空，去除 policyIdList 并添加到 query 中，同时 query. policyId 不包含  policyIdList
- 如果 namespaceCodeList 不为空不包含 system,通过 namespaceCodeList 和用户池 id 查找 namespaceList 并取出相关的 id，namespaceIdList

5、根据 query 条件根据时间倒序查询 PolicyAssignment 表的数据
- 如果 list 为空，直接返回
- 如果 list 不为空，

