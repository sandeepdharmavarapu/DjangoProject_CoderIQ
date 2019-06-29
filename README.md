# DjangoProject_CoderIQ
The project exposes 3 APIs and below are the details.
* Problem1 API: This API sets the cache limit (0-30) and updates the cache(which is a json file) with the data consumed from a web socket and closes the connection once the limit is reached. It can be accessed at path /silicon_valley_starter/problem1
* Problem2 API: This API handles the input query parameter string and returns the summaries accordingly fetched from the cache(cache.json created from the problem1 POST API). It can be accessed at path /silicon_valley_starter/problem2
* Problem3 API: This API returns all the summaries fetched from cache which have 'Richard' and 'Erlich'. It can be accessed at path /silicon_valley_starter/problem3
