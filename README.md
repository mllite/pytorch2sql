# pytorch2sql

This tool performs SQL Code generation for deploying PyTorch models on SQL databases.

Thanks to a scikit-learn wrapper (skorch), this tool uses the same framework used by Sklearn2sql. Sklearn2sql provides a framework for translating scikit-learn predictive models into a SQL code for deployment purposes. Using this framework, for example, it is possible for a C, perl or java developper to deploy such a model simply by executing the generated SQL code. The system supports the major market databases (db2, firebird, hive, impala, monetdb, MS SQL Server, mysql, oracle, pgsql, sqlite and teradata). Sklearn2sql has been tested and benchamrksed in production with very complex and large machine learning models.

It supports basic pytorch models (core layers and activation functions) for classification and regression tasks. It also has some support for convolutional models (with convolutional and pooling layers) as well as recurrrent models (RNN, LSTM, GRU, ...)

https://github.com/antoinecarme/sklearn2sql-demo

https://github.com/antoinecarme/sklearn2sql_heroku

Demo script : https://github.com/antoinecarme/pytorch2sql/blob/master/test_client.py
