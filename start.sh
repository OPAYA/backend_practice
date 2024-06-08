#!/bin/sh
export ENV=local

uvicorn app.main:app --reload