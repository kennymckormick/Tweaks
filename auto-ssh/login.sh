#!/usr/bin/expect
eval spawn ssh username@server
expect "*Verification code:*"
send [exec cat dyn_code.txt]
send "\r"
expect "Password:"
send [exec cat password.txt]
send "\r"
interact
