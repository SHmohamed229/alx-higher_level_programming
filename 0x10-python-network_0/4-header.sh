#!/bin/bash
# this script for to send custom headers to servers
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
