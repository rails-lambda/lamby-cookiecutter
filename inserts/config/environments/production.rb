
  # {% include "_cctmp/class_name.txt" %}
  # ----------
  logger = ActiveSupport::Logger.new(STDOUT)
  logger.formatter = ActiveSupport::Logger::SimpleFormatter.new
  config.logger    = ActiveSupport::TaggedLogging.new(logger)
  config.public_file_server.headers = {
    'Cache-Control' => "public, max-age=#{30.days.seconds.to_i}",
    'X-Lamby-Base64' => '1'
  }
  config.log_level = :info
  config.lograge.enabled = true
  config.lograge.formatter = Lograge::Formatters::Json.new
  config.lograge.custom_payload do |controller|
    { requestid: controller.request.request_id }
  end
end
