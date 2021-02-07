import logging as LogFactory

LogFactory.basicConfig(
    format="{\"time\": \"%(asctime)s\","
           " \"log\": \"%(filename)s:%(funcName)s:%(lineno)s\","
           " \"level\": \"%(levelname)s\","
           " \"message\": \"%(message)s\"}",
    level=LogFactory.INFO
)
