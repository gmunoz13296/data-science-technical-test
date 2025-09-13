# data-science-technical-test

## How to activate enviroment:
Copy and paste that command into ther terminal:
`.\venv\Scripts\activate`

## How to run:
Copy and paste that command into ther terminal:
`uvicorn main:app --reload`

## How to get test coverage:
Copy and paste that command into ther terminal:
`pytest --cov=. --cov-report=term-missing`

## How to use:
Put in the browser that url: `http://127.0.0.1:8000/docs`, this is the swagger service running.
Now you can use the endpoint: `classifier/classify`, that endpoint accepts the follow param:

`{
  "numbers": [
    0,1
  ],
  "algorithm": ""
}`

The property `numbers` is a list of integers that will be classifiers into the classes:
`FizzBuzz, Fizz, Buzz, None` according the exercise given.
The property `algorithm` is to select the algorithm you can use. For this example the `LogisticRegression` is the only implemented, and if you don't provide any value in that property that algorithm will be use, in other case an error could be throw.
There is an easy way to incorporate a new algorithm.

