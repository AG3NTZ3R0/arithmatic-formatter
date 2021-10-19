import re

def arithmetic_arranger(problems, show_sol=False):
  """Format a given list of problems vertically, side-by-side."""
  error = False
  num1_str = ""
  num2_str = ""
  break_str = ""
  sol_str = ""

  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
  else:
    for problem in problems:
      prob_nums = re.split('\s\S\s', problem)
      num1_len = len(prob_nums[0])
      num2_len = len(prob_nums[1])
      num_len_diff = abs(num1_len - num2_len)

      prob_op = re.findall('\s.\s', problem)
      prob_op = str(prob_op[0].strip())

      if num1_len > 4 or num2_len > 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        error = True
        break

      if re.search("\D", prob_nums[0]) or re.search("\D", prob_nums[1]):
        arranged_problems = "Error: Numbers must only contain digits."
        error = True
        break

      if prob_op == '+':
        sol = int(prob_nums[0]) + int(prob_nums[1])
      elif prob_op == '-':
        sol = int(prob_nums[0]) - int(prob_nums[1])
      else:
        arranged_problems = "Error: Operator must be '+' or '-'."
        error = True
        break

      if num1_len > num2_len:
        prob_nums[1] = prob_op + " " * (num_len_diff + 1) + prob_nums[1]
        prob_nums[0] = " " * (abs(len(prob_nums[0]) - len(prob_nums[1]))) + prob_nums[0]
        break_str_i = "-" * len(prob_nums[0])

      elif num1_len < num2_len:
        prob_nums[1] = prob_op + " " + prob_nums[1]
        prob_nums[0] = " " * (abs(len(prob_nums[0]) - len(prob_nums[1]))) + prob_nums[0]
        break_str_i = "-" * len(prob_nums[1])

      else:
        prob_nums[1] = prob_op + " " + prob_nums[1]
        prob_nums[0] = " " * (abs(len(prob_nums[0]) - len(prob_nums[1]))) + prob_nums[0]
        break_str_i = "-" * len(prob_nums[0])

      num1_str = num1_str + prob_nums[0] + " " * 4
      num2_str = num2_str + prob_nums[1] + " " * 4
      break_str = break_str + break_str_i + " " * 4
      sol_str = sol_str + " " * (len(prob_nums[0]) - len(str(sol))) + str(sol) + " " * 4
      
    if error == False:
      if show_sol:
        arranged_problems = num1_str.rstrip() + "\n" + num2_str.rstrip() + "\n" + break_str.rstrip() + "\n" + sol_str.rstrip()
      else:
        arranged_problems = num1_str.rstrip() + "\n" + num2_str.rstrip() + "\n" + break_str.rstrip()

  return arranged_problems