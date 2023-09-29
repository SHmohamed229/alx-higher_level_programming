#!/bin/bash
# this script for to send custom headers to servers
curl -s "$1" -H "X-School-User-Id: 98"
