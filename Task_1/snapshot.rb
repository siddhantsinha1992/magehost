#!/usr/bin/env ruby
require 'rest_client'
require 'json'

$time       = ENV['TIME']
$api_token  = ENV['DO_TOKEN']
$baseUrl    = "https://api.digitalocean.com/v2/"
$headers    = {:content_type => :json, "Authorization" => "Bearer #{$api_token}"}

class ResponseError < StandardError; end



def droplet_on?(droplet_id)
  url     = $baseUrl + "droplets/#{droplet_id}"
  droplet = get(url)['droplet']

  droplet['status'] == 'active'
end

def power_off(droplet_id)
  url = $baseUrl + "droplets/#{droplet_id}/actions"
  params = {'type' => 'power_off'}
  post(url, params)
end

def snapshot(droplet_id)
  url = $baseUrl + "droplets/#{droplet_id}/actions"
  params = {'type' => 'snapshot', 'name' => "Droplet #{droplet_id} + #{$time} "}
  post(url, params)
end

def get(url)
  response = RestClient.get(url, $headers){|response, request, result| response }
  puts response.code

  if response.code == 200
    JSON.parse(response)
  else
    raise ResponseError, JSON.parse(response)["message"]
  end
end

def post(url, params)
  response = RestClient.post(url, params.to_json, $headers){|response, request, result| response }

  if response.code == 201
    JSON.parse(response)
  else
    raise ResponseError, JSON.parse(response)["message"]
  end
end

droplets = ARGV

droplets.each do |droplet_id|
  puts "Attempting #{droplet_id}"

  begin
    if droplet_on?(droplet_id)
      power_off(droplet_id)

      while droplet_on?(droplet_id) do
        sleep 10
      end
      puts "Powered Off #{droplet_id}"
      sleep 10
    end

    snapshot(droplet_id)
    puts "Snapshotted #{droplet_id}"
  rescue ResponseError => e
    puts "Error Snapshotting #{droplet_id} - #{e.message}"
  end
end

