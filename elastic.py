import csv
import urllib2
from elasticsearch import Elasticsearch
if __name__=='__main__':
    response = urllib2.urlopen("http://apps.sloanahrens.com/qbox-blog-resources/kaggle-titanic-data/test.csv")
    csv_file_object = csv.reader(response)
    header = csv_file_object.next()
    header = [item.lower() for item in header]
    print("headers of CSV file=",header)
    data_dict=[]
    for row in csv_file_object:
        row_dict={}
        for i in range(len(header)):
            row_dict[header[i]]=row[i]
        data_dict.append(row_dict)
    es=Elasticsearch()
    for new_index,data_ele in enumerate(data_dict):
        es.index(index="rail",doc_type="data",id=new_index,body=data_ele)
    print(es.get(index="rail",doc_type="data",id=1))
    match=es.search(index="rail", body={"query": {"match": {'name':'Wilkes, Mrs. James (Ellen Needs)'}}})
    print("Result of Search=",match['hits']['hits'])
