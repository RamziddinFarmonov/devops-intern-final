job "hello" {
  datacenters = ["dc1"]
  type        = "batch"

  group "hello-group" {
    count = 1

    task "hello-task" {
      driver = "docker"

      config {
        image      = "localhost:5000/devops-intern-final:latest"
        force_pull = true
        command    = "/bin/sh"
        args       = ["-c", "python hello.py && sleep 20"]
      }

      resources {
        cpu    = 100
        memory = 128
      }
    }
  }
}