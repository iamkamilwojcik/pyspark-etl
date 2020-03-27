# pyspark-etl
Repository contains sample ETL project written in pyspark. 

## Prerequisites
1. Install Apache Spark for development purposes on your local box. [Installation steps](https://github.com/iamkamilwojcik/big-data-vagrant/blob/master/docs/spark_windows_setup.md) for Microsoft Windows 10 Professional.
1. Install [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) to create managable virtual environments.
## How to use
### IDE
1. Clone [pyspark-etl](https://github.com/iamkamilwojcik/pyspark-etl) repository.
1. Create virtual environment using pipenv.
1. Open console and type ```pipenv install``` to install required dependencies listed in pipfile.
1. To run ```template.py``` job on your local box navigate to ```/jobs/template.py``` and run the script. 
### spark-submit
1. Navigate to the root directory of pyspark-etl project.
1. Run```python build-dependencies.py``` to build job dependencies. It should create ```packages.zip``` file that contains all libraries installed to your virtual environment, base and utils catalog from pyspark-etl project. 
1. Use spark-submit command to send ```template.py``` job to remote cluster:   
```spark-submit --master spark://[your_master_node] -py-files [path_to_packages_file]/packages.zip template.py```   
Example:   
```C:\PycharmProjects>spark-submit --master spark://localhost:7077 --py-files packages.zip template.py```

