## DataTruth Programming Task

So we can see how you'd fit in on our team, we'd like to see how you tackle new challenges.

It is estimated that you might spend around 3-4 hours on this task. Please do not spend any more than 5 hours in total on the core requirements. If you're really enjoying it and decide to spend more time than that by getting into the stretch goals, that's cool too but is by no means expected.

**You are not expected to complete the task, what is more interesting to us is to see how you think and go about solving problems :-)**

### Preparation

Before starting this task, we recommend that you have:

- Your favourite computer and development tools / IDE to hand;
- A few hours of un-distracted time ahead of you;
- Access to the internet;
- A mug of hot coffee (or tea, if you prefer!).

### In this task, you may use:

- NodeJS and Python, along with any combination of technologies, open source modules, frameworks and techniques you like;
- The internet, including Google, Stackoverflow etc to help with the task;
- Any type of data store, although we have included some basic backend scaffolding to get you started which you can use if you prefer.

You may also ask us any general questions you might have about the task.

### Scaffolding

You'll find some basic scaffolding code within the repo, you are not expected to use this but will hopefully find that using it speeds up the process of getting started.

We've provided you with:

- A basic server using Express with [BabelJS](https://babeljs.io) preconfigured and a basic test. See [`./server/README.md`](./server/README.md) for more info.
- A `.nvmrc` file to set the Node version using [NVM](https://github.com/nvm-sh/nvm). You can use a different Node version if you wish, the scaffolding has been created and tested using `v16.13.0`.
- A `docker-compose.yml` file to start a Postgres database.
- Two files containing raw Olympic medals and country data in `raw-data`.

## Task 1 - Building the app

1. Clone this repository and create a branch called `hello-datatruth`;
2. Create a simple backend to act as the datastore for an application that will display Olympic medals data. Feel free to use the scaffolding provided as a starting point, or create a simple backend any other way you prefer;
3. Load the raw data provided in `raw-data` into your datastore;
4. Using **Python**, create a simple backend service that takes the raw data and transforms it into a list of countries, along with the number of Gold, Silver and Bronze medals they won during the 2012 Olympic Games.
5. Serve the resulting data via an API endpoint.
6. Create an *app* folder to contain your front end code;
7. In the *app* directory, create a simple app that displays your derived data in a basic Olympic Medals table to be viewed in a browser or on a device;
8. Commit your code and raise a pull request;
9. Your code will be reviewed by one of our senior technical team and we will get back to you.

If you wish to supply instructions on how to run or understand the construction of your app, then please provide those in a new README.md file within a `docs` folder.

If you can provide a link to view or download a demo of your app to go along with your code, then all the better.

### Stretch goals for bonus points:

If you find the task above easy and wish to continue, then feel free to improve your app. Here are some ideas but feel free to use your imagination rather than stick to these examples!:

- Allow rows to be sorted in ascending or descending order of each type of medal won;
- Computes some additional derivate data which you consider to be interesting and insightful e.g. most successful countries over time, most successful countries given population and display the output in a chart, if applicable;
- Improve your UI e.g. add country flag icons/images to the country names.

## Task 2 - A few questions

Please update the `questions.txt` file with your answers to the questions.

### Data Credits

The raw data in this task has been adapted and modified from an original set made available by The Guardian available on Kaggle at the following link: https://www.kaggle.com/datasets/the-guardian/olympic-games.

### Any questions?

Please just ask.

Good luck and thank you for taking the time to work on this task!