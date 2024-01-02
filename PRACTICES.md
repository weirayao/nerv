# Best Practices for Contributing to the Repository

## Code Style

1. Format the code using Black.
    1. Run ``./run_black.sh`` to apply Black to all of the code that you modified in the current branch.
2. Adhere to PEP 8 style when possible.  
    1. Run ``./run_flake8.sh`` to check for PEP 8 style for all of the code that you modified in the current branch.

## Documentation

1. Use the Sphinx docstring format for public classes and functions.
2. Use Sphinx to automatically format your docstrings as nicely formatted, searchable documentation web pages. Here are some helpful resources for getting started with Sphinx:
    1. Tutorial on getting started with Sphinx
    2. reStructured text and Sphinx cheatsheet - useful reference on how to format documentation in order for it to display properly 

## Tests

1. Add unit tests and integration tests for all new features.  Please check out  [Kensho](https://github.com/MetaMind/kensho) and [Optique](https://github.com/MetaMind/optique).
    1. We are currently using the pytest framework
    2. Read Salesforce’s Engineering Best Practices for more information about different types of tests.
2. Check that all tests pass before submitting a pull request.
    1. Run ``./run_unittests.sh`` to run all tests in the repo. To configure this script for your own repo:
        1. Add a ``__init__.py`` file into every directory that contains a test. This file can be blank. This allows test discovery to import the test cases.
        2. All test cases should be a subclass of unittest.TestCase.

## Code Review Process

### For developers

1. Develop your feature in a separate branch and submit a pull request when you are done for others to review. 
2. Add tests and documentation for your new feature in the same pull request.
3. Make sure that your code passes all unit tests and is formatted properly by running the code style and test scripts mentioned above.
4. Keep pull requests small. It makes it easier for others to review and catch mistakes. If your feature is big, try to split it into smaller pull requests.
5. Make your pull request easy to review by adding a description and inline comments on GitHub that guides reviewers through your changes and explains why you made these changes. These comments should not replace documentation in your code.
6. Request the reviewers that can give you the most thorough and correct review. This is typically the person who has worked on this part of the repo before.
7. Follow Google’s guide on handling review comments. Respond to reviewer comments professionally and emphatically. Clarify the reviewer’s questions by making changes in the code to help future readers of your code. 

Review Google’s guide to submitting pull requests for more information.

### For reviewers

1. Look for these qualities when you code review.
2. Make sure that the code passes all unit tests and is formatted properly by running the code style and test scripts mentioned above.
3. Review code as soon as possible, ideally within a day of receiving the pull request. Make sure the process between when you receive the code review request and the pull request is merged is fast. This helps the team develop features more quickly and keeps developers happy.
4. Follow Google’s guide on writing review comments. Write review comments with empathy.

Review Google’s guide on reviewing pull requests for more information.

## Creating a Library

1. Make the library easy to install.
    1. Add a requirements.txt file to install the dependencies of the library.
    2. Follow this tutorial on packaging your Python code. 
2. Configure logging for your library.
    1. Define a logger for each module like this.
    2. Document how your library uses logging.
    3. Don’t add any handlers other than the NullHandler (It prevents your library’s logged events being output to sys.stderr in the absence of logging configuration) because configuration of handlers should be taken care of by the library user who knows what is most appropriate for their application.
    4. To learn more about logging, refer to the Logging Cookbook.
