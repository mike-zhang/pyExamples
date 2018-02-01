#! /bin/sh

protoc -I=. --python_out=. addr.book.proto
touch addr/__init__.py



