# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
import websocket
import os
from django.shortcuts import render
from .forms import PostLimitForm, GetStringForm

def index(request):
    return HttpResponse("silicon valley starter is up!")

def problem1(request):
    ''' 
    This API sets the cache limit and updates the cache(which is a json file) 
    with the data consumed from a web socket and closes the connection once 
    the limit is reached.
    '''
    string=""
    if request.method == 'POST':
        form = PostLimitForm(request.POST)
        if form.is_valid():
            limit = form.cleaned_data.get("limit")
            #print(limit)
            ws = websocket.WebSocket()
            print(ws)
            ws.connect('ws://siliconvalleysummary.intuhire.com:8001/episodic-data/siliconValley')
            print(ws)
            ws.send("startdata")
            cache = {"result":[]}
            count = 0
            if limit > 30 or limit < 0:
                string = 'Cache limit not in range'
            elif os.path.exists("cache.json"):
                os.remove("cache.json")
                while count < limit:
                    print(limit)
                    result = ws.recv()
                    print(result)
                    cache["result"].append(str(result))
                    count+=1
                    print ("Received '%s'" % result)
                with open("cache.json", "wt") as file1:
                    json.dump(cache, file1)
                ws.close()
                string = "Cache limit set to {} and data is cached upto the specified limit".format(limit)
                print(string)
    else:
        form = PostLimitForm()
    return render(request, 'silicon_valley_postlimit.html', {'form': form, 'string': string})

#problem2, to look for a string in the cached summaries
def problem2(request):
    '''
    This API handles the input query parameter string and returns the summaries accordingly fetched from the cache(cache.json created from the problem1 POST API)
    '''
    summaries = []
    new_list = []
    print(request.method)
    if request.method == 'GET' and request.GET.get('string_text'):
        form = GetStringForm(request.GET)
        if form.is_valid():
            string_text = request.GET.get('string_text')
            print(string_text)
            with open("cache.json", "rt") as file1: 
                cache = json.load(file1)
            for item in cache["result"]:
                if string_text in item:
                    new_list.append(item)
            summaries = new_list if new_list else ["No summaries found"]
    else:
        form = GetStringForm()
    return render(request, 'silicon_valley_getstring.html', {'form': form, 'summaries': summaries})

#problem3, to return all summaries with both 'richard' and 'erlich' occurring 
def problem3(request):
    '''
    This API returns all the summaries fetched from cache which have 'Richard' and 'Erlich'
    '''
    summaries = []
    new_list = []
    if request.method == 'GET':
        with open("cache.json", "rt") as file1:
            cache = json.load(file1)
        print(cache)
        for item in cache["result"]:
            if 'Richard' in item or 'Erlich' in item:
                new_list.append(item) 
        print(new_list)  
        summaries = new_list if new_list else ["No summaries found"]
    return render(request, 'silicon_valley_getspecific.html', {'summaries': summaries})
