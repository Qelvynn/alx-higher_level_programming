#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);
      const completed = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (!completed[todo.userId]) {
            completed[todo.userId] = 0;
          }
          completed[todo.userId]++;
        }
      });

      const userStats = Object.entries(completed).map(([userId, count]) => ({
        userId: userId,
        completedTasks: count
      }));

      console.log(userStats.length > 0 ? JSON.stringify(userStats, null, 2) : 'No completed tasks found.');
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error fetching data from the API:', error);
  }
});
