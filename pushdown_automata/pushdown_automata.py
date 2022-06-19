# I: pda_rules.pds, input_string (e.g. aaabbb)
# pda_rules schema: if(current_state, input_char, pop_char), then(new_state, push_char)
# O: Accept (if the input is valid), or Reject
# usage: python pushdown_automata.py pda_rules.pda

import sys, re
from collections import defaultdict

# The PDA programming language has rules of the form:
#   (current state, input character, pop from stack, new state, push to stack)
# Intuitive, a rule is applicable if:
#  - the current PDA state is <current state>, and
#  - the current input character is <input character>, and
#  - the current top of the stack is <pop from stack>.
# After applying an applicable rule, the new PDA is <new state> and
# the <push to stack> character is pushed onto the stack.
#
# The following special characters are defined:
#  - '_' indicates the bottom of the stack and the end of the input
#  - '?' as <pop from stack> indicates that no character should be popped
#    off the stack when this rule is applied. Such a "wildcard" rule is
#    applicable regardless what character is the top of the stack.
#  - '?' as <push to stack> indicates that no character should be pushed
#    onto the stack when this rule is applied
# The PDA starts in state '0' and accepts the input if it terminates in
# state 'A' when the input has been consumed.


ANBN_CODE = """#
# Accepts strings of the form a^n b^n (Same number of a's and b's)
# For example: 'ab' or 'aaabbb', but not 'aab' or 'aabbb'.
#
# Accept empty string
0,_,_,A,?
# Push a on stack while seeing a's
0,a,?,0,a
# Move to state 1 and pop a's while seeing b's
0,b,a,1,?
1,b,a,1,?
# Accept if input and stack are empty
1,_,_,A,_
"""

PARENTHESIS_CODE = """#
# Accepts well-nested (()()())-expressions with extra a and b characters
# For example: '(())()' or 'a()()(ababbb)((b()))b', but not '(()' or ')'
#
# Accept empty string
0,_,_,A,?
# Push ( on stack when seeing (
0,(,?,0,(
# Pop from stack when seeing ) and stack is non-empty
0,),(,0,?
# Fail when seeing ) and stack is empty
0,),_,F,_
# Ignore a and b
0,a,?,0,?
0,b,?,0,?
# Accept when string and stack are empty
0,_,_,A,_
"""

PALINDROME_CODE = """#
# Non-deterministic PDA that accepts palindromes over {a, b, c}.
# For example: '', 'aa', or 'abccda', but not 'a', 'ab', or 'abccdaa'.
# "Forward-reading" is done in state '0' and "backward-reading"
# in state '1'.
#
# Accept empty string
0,_,_,A,_
# Read forward in state 0
0,a,?,0,a
0,b,?,0,b
0,c,?,0,c
# Non-deterministically transition to state 1 if we can
0,a,a,1,?
0,b,b,1,?
0,c,c,1,?
# Read backward in state 1
1,a,a,1,?
1,b,b,1,?
1,c,c,1,?
# Accept when string and stack are empty
1,_,_,A,_
"""


# read and parse program
def parse(program):
	rules = defaultdict(list)
	for line in program.splitlines():
		if line[0] != '#':
			(current_state, input_char, pop_char, new_state, push_char) = line.strip().split(',')
			rules[(current_state, input_char)].append([pop_char, new_state, push_char])
	return rules


def eval_non_det(input_string, rules):
	pass


def eval(input_string, rules): 
	"""Returns True if accepted; False if otherwise"""

	state = '0'
	stack = ['_']
	for input_char in input_string + '_':
		assert len(stack) > 0, "Programming error, found empty stack"

		top_of_stack = stack[-1]
		rule = lookup_rule(rules, state, input_char, top_of_stack)
		if rule is None: 
			print("No rule found")
			return False
		else:
			state = apply_rule(rule, stack)

		if state == 'A': 
			return True

	return False


def lookup_rule(rules, state, input_char, top_of_stack): 
	possible_rules = rules[(state, input_char)]
	for rule in possible_rules:
		(pop_char, _, _) = rule
		if pop_char == '?':
			return rule
		elif pop_char == top_of_stack:
			return rule
	# in cases where there is no matching rule
	return None


def apply_rule(rule, stack):
	(pop_char, new_state, push_char) = rule
	top_of_stack = stack[-1]
	if pop_char == top_of_stack: 
		stack.pop()
	if push_char != '?':
		stack.append(push_char)
	return new_state


def main(program_path, input_string):
	program = open(program_path, 'r').read()
	rules = parse(program)
	print(eval(input_string, rules))

main(sys.argv[1], sys.argv[2])


