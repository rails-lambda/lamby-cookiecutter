source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

gem 'rails'

gem 'aws-sdk-ssm'
gem 'dotenv-rails', require: 'dotenv/rails-now'
gem 'jbuilder'
gem 'lamby', require: false
gem 'webpacker'
gem 'sass-rails', '>= 6'

group :development do
  gem 'web-console'
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
