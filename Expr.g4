grammar Expr;

prog: curl_statement EOF;

curl_statement: 'curl' '-X' method=('GET' | 'POST' | 'PATCH' | 'DELETE') (header=content_type_header)? (data=json_payload)? requrl=url;

content_type_header: '-H Content-Type:' ('application/json')?;

url: 'http://studentdb.com/'('student' | 'schema')('/')?(UUIDV4)?('/')?;

json_payload: '-d' (data=json_obj)?;

json_obj:'{' pair (',' pair)* '}' | '{' '}';

pair: STRING ':' value;

arr: '[' value (',' value)* ']' | '[' ']';

value: STRING | NUMBER | arr | 'None';

STRING: '"' (SAFECODEPOINT)* '"';

fragment SAFECODEPOINT: ~ ["\\\u0000-\u001F];

NUMBER: '-'? INT ('.' [0-9] +)?;


fragment INT: '0' | [1-9] [0-9]*;

GET_METHOD:'GET';
POST_METHOD: 'POST';
PATCH_METHOD: 'PATCH';
DELETE_METHOD: 'DELETE';
PATH_STUDENT: 'student';
PATH_SCHEMA: 'schema';
CONTENT_TYPE: 'application/json';

UUIDV4: HEX_4 HEX_4 '-' HEX_4 '-' HEX_4 '-' HEX_4 '-' HEX_4 HEX_4 HEX_4;
HEX_4: HEX HEX HEX HEX;
HEX: [0-9a-fA-F];
NEWLINE : [\r\n]+;
WS : [ \t\n]+ -> skip;