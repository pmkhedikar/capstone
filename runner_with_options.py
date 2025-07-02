from behave.__main__ import main

if __name__ == "__main__":
    browser = "chromium"
    headless = "false"
    tags = "@login,@addTOCart,@placeorder"
    feature_file_path = "features/"

    main([
        '--define', f'browser={browser}',
        '--define', f'headless={headless}',
        '--tags', tags,
        feature_file_path,
        '--format=plain',
        '--outfile=behave.log',  # plain output to behave.log
        '--format=allure_behave.formatter:AllureFormatter',
        '--outfile=allure-results',  # Allure output to allure-results directory
        '--no-capture',
        '--no-capture-stderr',
        '-v',
    ])