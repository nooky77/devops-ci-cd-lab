##  Grafana-Prometheus

Ce texte présente une solution de monitoring complète basée sur **Grafana**, **Prometheus**, **Alertmanager** et **Node Exporter**, idéale pour surveiller l’état des applications et de l’infrastructure en production.

###  Composants principaux

- **Prometheus** : Outil open-source de collecte de métriques en format time-series. Il interroge des *exporters* (comme Node Exporter) et stocke les données avec des labels pour les différencier.
- **Grafana** : Plateforme de visualisation qui permet de créer des dashboards dynamiques, envoyer des alertes, et se connecter à diverses sources (Prometheus, MySQL, Elasticsearch…).
- **Alertmanager** : Gère les alertes générées par Prometheus et les envoie vers des canaux comme Slack, Email, Telegram, ou via des webhooks.
- **Node Exporter** : Exporte les métriques système (CPU, mémoire, disque…) depuis les machines surveillées.

---

##  Installation du stack via Git et Docker Compose

###  Prérequis
- Docker
- Docker Compose
- Git

###  Étapes d’installation

1. **Cloner le dépôt Git contenant tous les fichiers nécessaires** :
   ```bash
   git clone https://github.com/stefanprodan/dockprom
   cd dockprom
   ```

2. **Lancer les services avec Docker Compose** :
   ```bash
   docker-compose up -d
   ```

###  Accès aux interfaces
- **Grafana** : [http://localhost:3000](http://localhost:3000)  
  Identifiants par défaut : `admin` / `admin`
- **Prometheus** : [http://localhost:9090](http://localhost:9090)
- **Alertmanager** : [http://localhost:9000](http://localhost:9000)

---

## Dashboard Docker Host
- Home --> Dashboards --> Docker Host
- **Remarque** : un autre dashboard est inclus : Docker Containers pour le reporting sur les dockers

##  (optionnel) Comment importer un dashboard dans Grafana

1. Ouvrir Grafana → **Dashboards → Import**
2. Choisir :
   - Un fichier `.json` local
   - Ou un **ID de dashboard** depuis [Grafana.com](https://grafana.com/grafana/dashboards)
3. Sélectionner la source de données (ex. Prometheus)
4. Cliquer sur **Import**

💡 Exemple : Pour visualiser les métriques système, importer le dashboard officiel de **Node Exporter** (ID : `1860` sur Grafana.com).
