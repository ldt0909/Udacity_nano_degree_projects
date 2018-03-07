# Technical interview 
 
# Question 1:
def question1(s,t):
	t_length = len(t)
	s_length = len(s)
	if s_length < t_length:
		return False
	else:
		# substring
		#s_sort = sorted(s)
		t_sorted = sorted(t)
		#sorted_sub_s = []
		#substring_s = []
		for i in range(0,s_length - t_length + 1):
			sub_s_element = sorted(s[i:i+t_length])
			if t_sorted == sub_s_element:
				return True

		return False

#print question1("asdfd", "fd")
#print question1("asdfd", "asrrr")
#print question1("asdf d", "f d")
#print question1("as", "asdf")

# Question 2:
def question2(a):
	n = len(a)
	#sub_list_a = []
	longest_sub = ''
	# substring of a
	for i in range(0,n):
		for j in range(0,i):
			sub = a[j:i]
			reverse_sub = sub[::-1]
			if sub == reverse_sub:				
				if len(sub) > len(longest_sub):
					longest_sub = sub


				
				#sub_list_a.append(sub)
				#print sub_list_a
	
	#return max(sub_list_a, key = len)
	return longest_sub

		
print question2("asdbdbdou")
print question2("asksdhasdksjkasdjklas")
print question2("abcdecba")








	


