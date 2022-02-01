source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

gem 'rails', '~> 7.0.1'

gem 'aws-sdk-ssm'
gem 'dotenv-rails', require: 'dotenv/rails-now'
gem 'jbuilder'
gem 'importmap-rails'
gem 'lamby', require: false
gem 'sprockets-rails'

group :development do
  gem 'debug'
end

group :development, :test do
  gem 'byebug'
end

group :test do
  gem 'capybara'
  gem 'selenium-webdriver'
  gem 'webdrivers'
end

group :production do
  gem 'lograge'
end
