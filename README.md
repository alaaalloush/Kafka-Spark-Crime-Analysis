# Kafka-spark-crime-analysis
This project provides statistical analysis of the San Francisco crime incidents using Apache Kafka and Spark Structured Streaming.

A Kafka server is used to produce data, and ingest data. Data analysis is done by Spark Structured Streaming to answer the question: what are the top types of crimes in San Fransisco?

Data used for this project is from Kaggle police-department-calls-for-service.json . this file has 199999 rows of data. Here is a sample row of this data:

{crime_id:"183653756", 
original_crime_type_name:"Traf Violation Cite", 
report_date:"2018-12-31T00:00:00.000", 
call_date:"2018-12-31T00:00:00.000", 
offense_date:"2018-12-31T00:00:00.000", 
call_time:"23:54", 
call_date_time:"2018-12-31T23:54:00.000", 
disposition:"ARR", 
address:"100 Blk Howard St", 
city:"San Francisco", 
state:"CA", 
agency_id:"1", 
address_type:"Geo-Override", 
common_location:""}

radio_code.json file contains description for disposition code:
{disposition_code:"ARR", description:"Arrest"}

# Development Environment
If you wish to develop the project locally, you will need to set up your environment properly as described below:

Spark 2.4.3

Scala 2.11.x

Java 1.8.x

Kafka build with Scala 2.11.x

Python 3.6.x or 3.7.x

### For Macs or Linux:
- Download Spark from https://spark.apache.org/downloads.html. Choose "Prebuilt for Apache Hadoop 2.7 and later."
- Unpack Spark in one of your folders (I usually put all my dev requirements in /home/users/user/dev).
- Download binary for Kafka from this location https://kafka.apache.org/downloads, with Scala 2.11, version 2.3.0. Unzip in your local directory where you unzipped your Spark binary as well. Exploring the Kafka folder, you’ll see the scripts to execute in bin folders, and config files under config folder. You’ll need to modify zookeeper.properties and server.properties.
- Download Scala from the official site, or for Mac users, you can also use brew install scala, but make sure you download version 2.11.x.
- Run below to verify correct versions: 

  java -version

  scala -version

- Make sure your ~/.bash_profile looks like below (might be different depending on your directory):

  export SPARK_HOME=/Users/dev/spark-2.4.3-bin-hadoop2.7
  
  export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
  
  export SCALA_HOME=/usr/local/scala/
  
  export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH
 
### For Windows:
Please follow the directions found in this helpful StackOverflow post: https://stackoverflow.com/questions/25481325/how-to-set-up-spark-on-windows

# How to run
Install requirements using conda install --file requirements.txt if you use conda for Python. If you use pip rather than conda, then use pip install -r requirements.txt.
