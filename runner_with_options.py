from behave.__main__ import main

if __name__ == "__main__":
    browser = "chromium"
    headless = "false"
    tags = "@login,@addTOCart@"
    test_type="ui"
    feature_file_path = "features/"

    main([
        '--define', f'browser={browser}',
        '--define', f'headless={headless}',
        '--define', f'test_type={test_type}',
        '--tags', tags,
        feature_file_path,
        '--format=plain',
        '--outfile=behave.log',
        '--format=allure_behave.formatter:AllureFormatter',
        '--outfile=allure-results',
    ])