# Cheeta: A Multi-Account Manager for Crypto Trading

## Introduction

Cheeta is a Multi-Account manager for crypto trading. It allows a "superuser" to place a "Market Hypothesis", which Cheeta communicates to all users that qualify to make a personalized trade, based on the given hypothesis. 

Each user has an "Account Manager", that is responsible for managing the user's accounts in different exchanges. A user can have its personalized settings and other pieces of information that impact the Account manager's decision to make a trade, examples:

- Portfolio Risk Management
- Exchange preferences
- Coin references
- Liquidity
- Order size capacity
- Orders History
- Open Orders 

Cheeta then groups the personalized trades validated by the account managers, placing them in the exchange order group, acting as a "Market Maker". 

There are a lot of opensource trading bots that allow you to easily place orders in a given exchange, other bots allow you to place orders in multiple exchanges, but none that allows you to manage multiple third-party accounts in multiple exchanges and other tasks related to fund managing.  

That's where Cheeta comes in, it takes care of all these details and allows you, the "superuser" to focus on your trading strategy. Be that of trying to beat the market by day trading or helping the market's liquidity by market-making. 

It's important to note that the strategy lives outside of Cheeta. Cheeta only receives a hypothesis, it cants create one. 

### When Should I use Cheeta? 

Let's say you are a crypto day trader (a good one) and decides to expand your capital, and gains, by accepting to manage someone else funds.

Congratulations, you are now responsible for managing a diverse group of clients.

It could be your mom, which 100% trust's you, but doesn't understand anything about crypto and only "invests" 100 USD. Or it could be your college friend that mined 10 Bitcoins a few years ago and doesn't want to hand you his keys to his wallet without any guarantees. 

- And what if your strategy involves multiple coin pairs and/or multiple exchanges?
- Your friend's order size may be 0.1 BTC, but what about your mom's order size?
- What if Binance doesn't accept your mom's 5 USD order because it's too low?
- How do you deploy and maintain multiple bots?
- What about your commission? 
- What if your friend wants to withdrawal 5 BTC?
- What if your mom wants to deposit 1000 USD?

Without Cheeta:
You => Strategy => Market Hypotesis => A lot of annoying taks => Trades => More annoying tasks => Commision (with possible miscalculations) 

With Cheeta:
You => Strategy => Market Hypotesis => Cheeta => Trades => Commission

### What are Market Hypotheses?

It's the result of your strategy, which decides what order should be placed in the crypto exchange. 

It could be as simple as: "Elon Musk bought Dogecoin, let's go to the moon." and as complex as a Recursive Neural Network written by Mathematicians with PhDs. 

In the end, they all produce a Hypothesis about the market, with a coin pair, price prediction, size, etc. 

Initially, Cheeta will make GET request to a predefined API, but in the future will have it's own CLI to place group orders on the go.  

The ultimate goal is that Cheeta becomes deployable and able to receive POST requests to place orders and act as a Back end for a web application that displays the accounts state for the "superuser" and regular users can check their balance and portfolio performance.


## ROADMAP

### PHASE 1: The First Avenger (IN DEVELOPMENT)
An MVP, Cheeta can manage one account with multiple coin pairs and exchanges. User portfolio and trades are stored in a Database and superuser commissions are easily accessible.

### PHASE 2: Avengers... Assemble
A scaled Cheeta that can manage multiple accounts and comes with a CLI. 

### PHASE 3: Infinity Backend
Cheeta runs a server that can receive trades as a POST request and access to the user's portfolio data via GET request. 

### PHASE 4: ENDCONTRACTS
There was an idea, to write smart-contracts and bring together, a group of traders and investors, to see if we can become something more...
