
#!/bin/bash
set -e

echo "Starting Nginx..."

sudo systemctl enable nginx
sudo systemctl restart nginx

echo "Nginx is running."
