FROM amazoncorretto:11-alpine-jdk
# Update the package manager and install necessary tools
RUN yum update -y \
    && yum install -y tar gzip which \
    && yum clean all

# Define environment variables
ENV MAVEN_VERSION=3.8.5
ENV MAVEN_HOME=/opt/maven

# Download and install Maven
RUN curl -fsSL http://www-eu.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz -o /tmp/apache-maven.tar.gz \
    && tar xzf /tmp/apache-maven.tar.gz -C /opt/ \
    && ln -s /opt/apache-maven-${MAVEN_VERSION} /opt/maven \
    && rm -f /tmp/apache-maven.tar.gz

# Add Maven binaries to the system PATH
ENV PATH=${MAVEN_HOME}/bin:${PATH}

# Verify Maven installation
RUN mvn --version

WORKDIR /app
COPY . /app
RUN javac sample.java
CMD ["java","sample"]
