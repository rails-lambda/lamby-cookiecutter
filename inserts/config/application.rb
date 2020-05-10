Bundler.require(*Rails.groups.tap { |groups|
  if Rails.env.development? || Rails.env.test?
    groups << 'assets'
  end
})
