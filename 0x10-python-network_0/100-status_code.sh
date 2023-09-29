#!/bin/bash
# Bash this script for display status code of server
curl -L -s -X HEAD -w "%{http_code}" "$1"
