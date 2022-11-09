def arithmetic_arranger(problems, answers = False):
    arranged_problems = problems
    problemList = []
    maxElementLength = []# Width for each problem
    #Check if no more than 5 problems supplied
    if len(problems) > 5:
      return "Error: Too many problems."

    # Split each element into operands and operator
    for element in problems:
      problemList.append(splitProblem(element))

    # Check operator
    for element in problemList:
      if checkOperator(element[1]) is False:
        return "Error: Operator must be '+' or '-'."

    # Check and convert each operand into digit. Do the math if all checks out on the same iteration.
    for index, element in enumerate(problemList):
      # Check if operands are no longer than 4 digits
      if len(element[0]) > 4 or len(element[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
      
      firstOperand = stringToDigit(element[0])
      secondOperand = stringToDigit(element[2])

      # Check if operands have valid digits
      if firstOperand == -1 or secondOperand == -1:
        return "Error: Numbers must only contain digits."
      
      problemList[index][0] = firstOperand
      problemList[index][2] = secondOperand
      problemList[index].append(doMath(firstOperand, secondOperand, problemList[index][1]))

    # Work out each problems character width
    for element in problemList:
      maxElementLength.append(maxWidth(element))
      
    # Build final string
    arranged_problems = constructString(problemList, maxElementLength, answers)
  
    return arranged_problems

def checkOperator(operator):
    if operator == "+" or operator == "-":
      return True
    return False

def splitProblem(problem):
  return problem.split(" ")

# Convert string to digit and check its length
def stringToDigit(element):
  try:
    return int(element)
  except:
    return -1

def doMath(firstOperand, secondOperand, operator):
  if operator == "+":
    return firstOperand + secondOperand
  else:
    return firstOperand - secondOperand

def maxWidth(problemSet):
  firstCharacterLength = len(str(problemSet[0]))
  secondCharacterLength = len(str(problemSet[2]))
  characterLength = 0
  
  if firstCharacterLength > secondCharacterLength:
    characterLength = firstCharacterLength
  else:
    characterLength = secondCharacterLength
  return characterLength + 2# +2 is for operator and space after it

# Main function for building the final string for arranged problems
def constructString(problemList, characterLengthList, answers = False):
  fullString = ""

  # Construct the first line of arranged problems
  for index, element in enumerate(problemList):
    fullString += whiteSpaceWithChar(element[0], characterLengthList[index])
    if index == len(problemList) - 1:
      continue# Skip adding white spaces after the last element
    # Add white spaces at the end of each element, except last one (breaks loop with ifs before)
    fullString += whiteSpaces()
    
  # Add a new line character
  fullString += "\n"
  
  # Construct the second line of arranged problems
  for index, element in enumerate(problemList):
    fullString += element[1] + " " + whiteSpaceWithChar(element[2], characterLengthList[index] - 2)# -2 to exclude operator spacing as it is added in this line separately
    if index == len(problemList) - 1:
      continue# Skip adding white spaces after the last element
    # Add white spaces at the end of each element, except last one (breaks loop with ifs before)
    fullString += whiteSpaces()
    
  # Add a new line character
  fullString += "\n"
    
  # Construct the third line of arranged problems (dashes)
  for index, element in enumerate(problemList):
    fullString += addDash(characterLengthList[index])
    if index == len(problemList) - 1:
      continue# Skip adding white spaces after the last element
    # Add white spaces at the end of each element, except last one (breaks loop with ifs before)
    fullString += whiteSpaces()

  # Construct the fourth line if needed
  if answers is True:  
    # Add a new line character
    fullString += "\n"
    for index, element in enumerate(problemList):
      fullString += whiteSpaceWithChar(element[3], characterLengthList[index])
      if index == len(problemList) - 1:
        continue# Skip adding white spaces after the last element
      # Add white spaces at the end of each element, except last one (breaks loop with ifs before)
      fullString += whiteSpaces()
    
    
  return fullString

def whiteSpaceWithChar(character, fullLength):
  string = ""
  spaceLength = fullLength - len(str(character))
  
  while spaceLength > 0:
    string +=" "
    spaceLength -= 1

  string += str(character)
  return string

# Add 4 white spaces
def whiteSpaces():
  return "    "
  
# Add a defined number of dashes
def addDash(length):
  dashes = ""
  i = length
  while i > 0:
    dashes += "-"
    i -= 1
  return dashes
