
  # {% include "_cctmp/class_name.txt" %}
  # ----------
  config.public_file_server.headers = {
    'Cache-Control' => "public, max-age=#{30.days.seconds.to_i}",
    'X-Lamby-Base64' => '1'
  }
  config.log_level = :info
  config.lograge.enabled = true
  config.lograge.formatter = Lograge::Formatters::Json.new
end
