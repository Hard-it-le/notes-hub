## docker-compose 安装

```yml
version: '3.2'  
  
services:  
  elasticsearch:  
    image: elasticsearch:7.17.4  
    volumes:  
      - ./es/plugins:/usr/share/elasticsearch/plugins #插件文件挂载  
      - ./es/data:/usr/share/elasticsearch/data #数据文件挂载  
    ports:  
      - "9200:9200"  
#      - "9300:9300"  不理解为什么开放 9300    container_name: elasticsearch  
    restart: always  
    environment:  
      - "TZ=Asia/Shanghai"  
      - "cluster.name=elasticsearch" #设置集群名称为elasticsearch  
      - "discovery.type=single-node" #以单一节点模式启动  
      - "ES_JAVA_OPTS=-Xms1024m -Xmx1024m" #设置使用jvm内存大小  
    networks:  
      - elk  
    deploy:  
      resources:  
        limits:  
          cpus: '0.75'  
          memory: 4096M  
  
networks:  
  elk:  
    name: elk  
    driver: bridge  
```

### ik 分词器安装

```bash
#  ik 分词器的安装  
# 集群 
docker-compose exec elasticsearch elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.17.4/elasticsearch-analysis-ik-7.17.4.zip
# 单点 
bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.17.4/elasticsearch-analysis-ik-7.17.4.zip
```