provider "kubernetes" {
    config_path = "~/.kube/config"
}

resource kubernetes_namespace "mlops" {
    metadata {
        name = "mlops"
    }
    lifecycle {
        ignore_changes = [metadata]
    }
}

resource "kubernetes_namespace" "argocd" {
    metadata {
      name = "argocd"
    }
    lifecycle {
        ignore_changes = [metadata]
    }
}

resource "kubernetes_namespace" "tekton" {
    metadata {
      name = "tekton-pipelines"
    }
    lifecycle {
        ignore_changes = [metadata]
    }
}