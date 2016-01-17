# GorynychDiamondFoxC2Tracker

Usage:

(1) Run GorynychTracker.py to create monolithic "GorynychHostTracker.sqlite" database with columns "rdate", "url", "ip", "rtype";

(2) Run GorynychIPConverter.py to convert hostnames to cities using http://ip-api.com JSON API and post data to "where.data";

(3) Run Geoload.py to parse "where.data", obtain lat/long values using Google MAP API, and store values in another database "geodata.sqlite";

(4) Run Geodump.py to map the data from "geodata.sqlite" to Javascript file "where.js";

(5) View the Google-mapped values in "where.html" that points to "where.js".
