FROM amazoncorretto:11-alpine-jdk
# Update the package manager and install necessary tools
RUN apk update \
    && apk add maven
    
# Verify Maven installation
RUN mvn --version

WORKDIR /app
COPY . /app
RUN javac sample.java
CMD ["java","sample"]
