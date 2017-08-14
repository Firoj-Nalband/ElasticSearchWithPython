1. First downloaded ES(elasticsearch5.5.1 given), it’s as simple as running bin/elasticsearch and you will have your ES cluster with one node running! You can interact with it at http://localhost:9200/

If you hit it you will get something like this:

{
  "status" : 200,
  "name" : "Delphine Courtney",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "1.4.2",
    "build_hash" : "927caff6f05403e936c20bf4529f144f0c89fd8c",
    "build_timestamp" : "2014-12-16T14:11:12Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.2"
  },
  "tagline" : "You Know, for Search"
}
It's optional, Creating another node is as simple as: 'bin/elasticsearch -Des.node.name=Node-2'
It automatically detects the old node as its master and joins our cluster. By default we will be able to communicate with this new node using the 9201 port http://localhost:9201. Now we can talk with each node and receive the same data, they are supposed to be identical.

2. pip install elasticsearch
