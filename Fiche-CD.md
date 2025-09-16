# FICHE – CD DEVOPS 

> Lorsque toutes les livraisons sont fusionnées, vous allez procéder au déploiement de l'image sur votre compte Docker Hub.

## Travail à faire

1. Synchronier votre dépôt avec la version finale du formateur
    - dans Github : cliquer sur le _bouton_ "`Sync Fork`"
    - en local, effectuer un pull : `git pull`

2. Initialiser les Secrets dans Github
    - générer votre token Docker Hub : `Account-setting -> Personal access tokens -> Generate new token`
    - enregistrer DOCKER_USERNAME et DOCKERHUB_TOKEN dans Github
      - `settings de votre repo -> Secrets & Variables -> Actions -> New repo Secret`

3. Compléter le ci.yml par les instructions suivantes

```yml
  docker-build:
    runs-on: ubuntu-latest
    needs: lint-test
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build Docker image
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/devops-tp .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/devops-tp

```
4. faire un push

5. si tout se passe bien, votre nouvelle image est sur Docker Hub

6. tester cette image en local
    - docker pull docker.io/username/devops-tp:latest
    - docker run -d -p 5001:5000 <id_de_votre_image_telechargee>
    - tester : curl localhost:5001
    - vérifier sur le navigateur