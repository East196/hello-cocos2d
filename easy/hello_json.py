#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
value=u'[{"name":"\\xE6\\xAF\\x8D\\xE5\\xA9\\xB4\\xE4\\xBA\\xB2\\xE5\\xAD\\x90/\\xE6\\xAF\\x8D\\xE5\\xA9\\xB4\\xE7\\xA4\\xBE\\xE5\\x8C\\xBA","weight":"46"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE7\\x90\\x86\\xE8\\xB4\\xA2\\xE8\\xB4\\xAD\\xE7\\x89\\xA9","weight":"49"},{"name":"\\xE9\\x87\\x91\\xE8\\x9E\\x8D\\xE8\\xB4\\xA2\\xE7\\xBB\\x8F","weight":"52"},{"name":"\\xE5\\xBD\\xB1\\xE8\\xA7\\x86\\xE9\\x9F\\xB3\\xE4\\xB9\\x90","weight":"67"},{"name":"\\xE8\\xB5\\x84\\xE8\\xAE\\xAF","weight":"67"},{"name":"\\xE5\\x8C\\xBB\\xE7\\x96\\x97\\xE5\\x81\\xA5\\xE5\\xBA\\xB7","weight":"58"},{"name":"\\xE6\\x95\\x99\\xE8\\x82\\xB2\\xE5\\x9F\\xB9\\xE8\\xAE\\xAD","weight":"67"},{"name":"\\xE6\\x95\\x99\\xE8\\x82\\xB2\\xE6\\xB0\\xB4\\xE5\\xB9\\xB3/\\xE9\\xAB\\x98\\xE4\\xB8\\xAD\\xE5\\x8F\\x8A\\xE4\\xBB\\xA5\\xE4\\xB8\\x8B","weight":"45"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE8\\xB5\\x84\\xE8\\xAE\\xAF\\xE9\\x98\\x85\\xE8\\xAF\\xBB","weight":"96"},{"name":"\\xE4\\xB9\\xA6\\xE7\\xB1\\x8D\\xE9\\x98\\x85\\xE8\\xAF\\xBB","weight":"40"},{"name":"\\xE6\\x88\\xBF\\xE4\\xBA\\xA7","weight":"59"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE5\\xBA\\x94\\xE7\\x94\\xA8\\xE5\\xB8\\x82\\xE5\\x9C\\xBA","weight":"72"},{"name":"\\xE5\\xAE\\xB6\\xE7\\x94\\xB5\\xE6\\x95\\xB0\\xE7\\xA0\\x81","weight":"9"},{"name":"\\xE4\\xBD\\x93\\xE8\\x82\\xB2\\xE5\\x81\\xA5\\xE8\\xBA\\xAB","weight":"26"},{"name":"\\xE6\\xAF\\x8D\\xE5\\xA9\\xB4\\xE4\\xBA\\xB2\\xE5\\xAD\\x90","weight":"60"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8","weight":"98"},{"name":"\\xE6\\xB8\\xB8\\xE6\\x88\\x8F/\\xE6\\x89\\x8B\\xE6\\x9C\\xBA\\xE6\\xB8\\xB8\\xE6\\x88\\x8F","weight":"56"},{"name":"\\xE4\\xB9\\xA6\\xE7\\xB1\\x8D\\xE9\\x98\\x85\\xE8\\xAF\\xBB/\\xE6\\x96\\x87\\xE5\\xAD\\xA6","weight":"40"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE7\\x94\\x9F\\xE6\\xB4\\xBB\\xE5\\xAE\\x9E\\xE7\\x94\\xA8","weight":"95"},{"name":"\\xE5\\xAE\\xB6\\xE7\\x94\\xB5\\xE6\\x95\\xB0\\xE7\\xA0\\x81/\\xE6\\xB4\\x97\\xE8\\xA1\\xA3\\xE6\\x9C\\xBA","weight":"7"},{"name":"\\xE6\\xB1\\xBD\\xE8\\xBD\\xA6","weight":"61"},{"name":"\\xE6\\xB8\\xB8\\xE6\\x88\\x8F/\\xE6\\xA8\\xA1\\xE6\\x8B\\x9F\\xE8\\xBE\\x85\\xE5\\x8A\\xA9","weight":"40"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE5\\xBD\\xB1\\xE9\\x9F\\xB3\\xE5\\x9B\\xBE\\xE5\\x83\\x8F","weight":"95"},{"name":"\\xE6\\xAF\\x8D\\xE5\\xA9\\xB4\\xE4\\xBA\\xB2\\xE5\\xAD\\x90/\\xE7\\xAB\\xA5\\xE8\\xBD\\xA6\\xE7\\xAB\\xA5\\xE5\\xBA\\x8A","weight":"9"},{"name":"\\xE5\\x95\\x86\\xE5\\x8A\\xA1\\xE6\\x9C\\x8D\\xE5\\x8A\\xA1","weight":"9"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE7\\xA4\\xBE\\xE4\\xBA\\xA4\\xE9\\x80\\x9A\\xE8\\xAE\\xAF","weight":"98"},{"name":"\\xE6\\xAF\\x8D\\xE5\\xA9\\xB4\\xE4\\xBA\\xB2\\xE5\\xAD\\x90/\\xE5\\xAD\\x95\\xE5\\xA9\\xB4\\xE4\\xBF\\x9D\\xE5\\x81\\xA5","weight":"64"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE7\\xB3\\xBB\\xE7\\xBB\\x9F\\xE5\\xB7\\xA5\\xE5\\x85\\xB7","weight":"98"},{"name":"\\xE4\\xBD\\x93\\xE8\\x82\\xB2\\xE5\\x81\\xA5\\xE8\\xBA\\xAB/\\xE6\\x9E\\x81\\xE9\\x99\\x90\\xE8\\xBF\\x90\\xE5\\x8A\\xA8","weight":"8"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE6\\xAF\\x8D\\xE5\\xA9\\xB4\\xE8\\x82\\xB2\\xE5\\x84\\xBF","weight":"30"},{"name":"\\xE5\\xBD\\xB1\\xE8\\xA7\\x86\\xE9\\x9F\\xB3\\xE4\\xB9\\x90/\\xE9\\x9F\\xB3\\xE4\\xB9\\x90","weight":"63"},{"name":"\\xE6\\x97\\x85\\xE6\\xB8\\xB8\\xE9\\x85\\x92\\xE5\\xBA\\x97","weight":"59"},{"name":"\\xE4\\xBD\\x93\\xE8\\x82\\xB2\\xE5\\x81\\xA5\\xE8\\xBA\\xAB/\\xE5\\x81\\xA5\\xE8\\xBA\\xAB\\xE6\\x93\\x8D","weight":"9"},{"name":"\\xE5\\x8C\\xBB\\xE7\\x96\\x97\\xE5\\x81\\xA5\\xE5\\xBA\\xB7/\\xE5\\x85\\xBB\\xE7\\x94\\x9F\\xE4\\xBF\\x9D\\xE5\\x81\\xA5","weight":"29"},{"name":"\\xE8\\xBD\\xAF\\xE4\\xBB\\xB6\\xE5\\xBA\\x94\\xE7\\x94\\xA8/\\xE6\\x97\\x85\\xE6\\xB8\\xB8\\xE5\\x87\\xBA\\xE8\\xA1\\x8C","weight":"73"},{"name":"\\xE6\\x97\\x85\\xE6\\xB8\\xB8\\xE9\\x85\\x92\\xE5\\xBA\\x97/\\xE5\\x9B\\xBD\\xE5\\x86\\x85\\xE6\\xB8\\xB8","weight":"48"},{"name":"\\xE6\\xB8\\xB8\\xE6\\x88\\x8F","weight":"56"},{"name":"\\xE5\\xB9\\xB4\\xE9\\xBE\\x84/25-34","weight":"91"},{"name":"\\xE5\\x8C\\xBB\\xE7\\x96\\x97\\xE5\\x81\\xA5\\xE5\\xBA\\xB7/\\xE8\\x8D\\xAF\\xE5\\x93\\x81","weight":"9"},{"name":"\\xE6\\x80\\xA7\\xE5\\x88\\xAB/\\xE7\\x94\\xB7","weight":"72"},{"name":"\\xE7\\xBD\\x91\\xE7\\xBB\\x9C\\xE8\\xB4\\xAD\\xE7\\x89\\xA9","weight":"59"},{"name":"\\xE6\\xB1\\x82\\xE8\\x81\\x8C\\xE5\\x88\\x9B\\xE4\\xB8\\x9A","weight":"41"},{"name":"\\xE6\\x88\\xBF\\xE4\\xBA\\xA7/\\xE4\\xBA\\x8C\\xE6\\x89\\x8B\\xE6\\x88\\xBF","weight":"30"},{"name":"\\xE5\\xBB\\xBA\\xE6\\x9D\\x90\\xE5\\xAE\\xB6\\xE5\\xB1\\x85","weight":"43"},{"name":"\\xE6\\x89\\x80\\xE5\\x9C\\xA8\\xE8\\xA1\\x8C\\xE4\\xB8\\x9A/\\xE5\\xBB\\xBA\\xE7\\xAD\\x91\\xE6\\x88\\xBF\\xE5\\x9C\\xB0\\xE4\\xBA\\xA7","weight":"41"},{"name":"\\xE4\\xBC\\x91\\xE9\\x97\\xB2\\xE7\\x88\\xB1\\xE5\\xA5\\xBD","weight":"44"}]'
# print value.decode("utf-8")
# print type(value.decode("utf-8"))
# print value.encode("utf-8")
# print type(value.encode("utf-8"))
# print value.encode("utf-8").decode("utf-8")

import re
regex = re.compile(r'\\(?![/u"])')
value = regex.sub(r"\\\\", value)
value=json.loads(value.encode("utf-8"))
print(value)

# print value[0]['name'].encode('ascii')
print(value[0]['name'].decode("string_escape"))

print('\xE6\xAF\x8D\xE5\xA9\xB4\xE4\xBA\xB2\xE5\xAD\x90/\xE6\xAF\x8D\xE5\xA9\xB4\xE7\xA4\xBE\xE5\x8C\xBA')
