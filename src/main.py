from replit import clear
#HINT: You can call clear() to clear the output in the console.
clear()
from art import logo

print(logo)
# to hold the dect key and value we
# are going to creat new dict variable or object
bider = {}
dict_price = {}
# and to see the which key to create
bider_empty_key=[]
def fill_the_dict(user_name, user_price):
  # now with the help of the key of the existing dictionary to the new empty dictiionary..
  bider["user_name"] = user_name
  bider["user_money"] = user_price
  bider_empty_key.append(bider)

# to keep track of the highstt money we are going to create another object called highe
# creating the function that will find the avavrage..
def finding_the_avarage(bidding_rocored):
  higher = 0
  user = ""
  for bidder in bidding_rocored:
    if bidding_rocored[bidder] >higher :
      higher = bidding_rocored[bidder]
      user = bidder
  print(f"The winer is : {user} with a bid of$ : {higher}")
# creating the boolean variable
user_input = True
# now i am going to print the greeting message
print("Welcome to the auction program")
# while the user_input is not going to be false then the loop will continue
while user_input:
  name = input("Enter your name?: ")
  price = int(input("What's your bid? : $"))
  dict_price[name] = price
  fill_the_dict(name,price)
  user_choose = input("Are there any other bidders? 'yes' or 'no'.").lower()
  # now checking the if the user typed yes or no if yes  then it will continue or choose no then the program will exit
  if user_choose == 'no':
    user_input = False
    # now printing the value of the dectionarry
    finding_the_avarage(dict_price)
  elif user_choose == "yes":
    clear()
