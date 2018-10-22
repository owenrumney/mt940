# Bit of Both

## Overview

A header file with the headings required and a single file with all the data in it.

The goal is to turn the data file into a load of json.

## Vanilla
This is just using bog standard python to process line by line.

``` bash
python vanilla.py
```

If you look in `vanilla.output` you can see that it just printed the json as expected

## Spark
This one uses spark and distribute the lines in the file to our multiple servers (not really) - in its simplest form, you submit it with spark submit

``` bash
spark-submit spark.py
```

When you look at `spark.output` you can see a lot more info was written, but towards the bottom of the output you can see the json was written.
