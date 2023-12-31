# Ответы к домашнему заданию по занятию 9 «Процессы CI/CD»

## Знакомоство с SonarQube

### Основная часть

1. Создайте новый проект, название произвольное.
2. Скачайте пакет sonar-scanner, который вам предлагает скачать SonarQube.
3. Сделайте так, чтобы binary был доступен через вызов в shell (или поменяйте переменную PATH, или любой другой, удобный вам способ).
4. Проверьте `sonar-scanner --version`.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd$ sonar-scanner --version
INFO: Scanner configuration file: /home/fedor/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/sonar-scanner-4.8.0.2856-linux/conf/sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: SonarScanner 4.8.0.2856
INFO: Java 11.0.17 Eclipse Adoptium (64-bit)
INFO: Linux 5.15.0-75-generic amd64
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd$
```
6. Запустите анализатор против кода из директории [example](./example) с дополнительным ключом `-Dsonar.coverage.exclusions=fail.py`.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/example$ sonar-scanner   -Dsonar.projectKey=test_project   -Dsonar.sources=.   -Dsonar.host.url=http://158.160.54.56:9000   -Dsonar.login=025d5c514e4b3d5b02b2ba05c1cd40c32d733e53 -Dsonar.coverage.exclusions=fail.py 
INFO: Scanner configuration file: /home/fedor/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/sonar-scanner-4.8.0.2856-linux/conf/sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: SonarScanner 4.8.0.2856
INFO: Java 11.0.17 Eclipse Adoptium (64-bit)
INFO: Linux 5.15.0-75-generic amd64
INFO: User cache: /home/fedor/.sonar/cache
INFO: Analyzing on SonarQube server 9.1.0
INFO: Default locale: "en_US", source code encoding: "UTF-8" (analysis is platform dependent)
INFO: Load global settings
INFO: Load global settings (done) | time=107ms
INFO: Server id: 9CFC3560-AYmlwUZC-rwKJ7EY3aNq
INFO: User cache: /home/fedor/.sonar/cache
INFO: Load/download plugins
INFO: Load plugins index
INFO: Load plugins index (done) | time=63ms
INFO: Load/download plugins (done) | time=12020ms
INFO: Process project properties
INFO: Process project properties (done) | time=10ms
INFO: Execute project builders
INFO: Execute project builders (done) | time=2ms
INFO: Project key: test_project
INFO: Base dir: /home/fedor/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/example
INFO: Working dir: /home/fedor/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/example/.scannerwork
INFO: Load project settings for component key: 'test_project'
INFO: Load project settings for component key: 'test_project' (done) | time=37ms
INFO: Load quality profiles
INFO: Load quality profiles (done) | time=82ms
INFO: Load active rules
INFO: Load active rules (done) | time=2039ms
INFO: Indexing files...
INFO: Project configuration:
INFO:   Excluded sources for coverage: fail.py
INFO: 1 file indexed
INFO: 0 files ignored because of scm ignore settings
INFO: Quality profile for py: Sonar way
INFO: ------------- Run sensors on module test_project
INFO: Load metrics repository
INFO: Load metrics repository (done) | time=43ms
INFO: Sensor Python Sensor [python]
WARN: Your code is analyzed as compatible with python 2 and 3 by default. This will prevent the detection of issues specific to python 2 or python 3. You can get a more precise analysis by setting a python version in your configuration via the parameter "sonar.python.version"
INFO: Starting global symbols computation
INFO: 1 source file to be analyzed
INFO: Load project repositories
INFO: Load project repositories (done) | time=25ms
INFO: 1/1 source file has been analyzed
INFO: Starting rules execution
INFO: 1 source file to be analyzed
INFO: 1/1 source file has been analyzed
INFO: Sensor Python Sensor [python] (done) | time=681ms
INFO: Sensor Cobertura Sensor for Python coverage [python]
INFO: Sensor Cobertura Sensor for Python coverage [python] (done) | time=8ms
INFO: Sensor PythonXUnitSensor [python]
INFO: Sensor PythonXUnitSensor [python] (done) | time=0ms
INFO: Sensor CSS Rules [cssfamily]
INFO: No CSS, PHP, HTML or VueJS files are found in the project. CSS analysis is skipped.
INFO: Sensor CSS Rules [cssfamily] (done) | time=0ms
INFO: Sensor JaCoCo XML Report Importer [jacoco]
INFO: 'sonar.coverage.jacoco.xmlReportPaths' is not defined. Using default locations: target/site/jacoco/jacoco.xml,target/site/jacoco-it/jacoco.xml,build/reports/jacoco/test/jacocoTestReport.xml
INFO: No report imported, no coverage information will be imported by JaCoCo XML Report Importer
INFO: Sensor JaCoCo XML Report Importer [jacoco] (done) | time=2ms
INFO: Sensor C# Project Type Information [csharp]
INFO: Sensor C# Project Type Information [csharp] (done) | time=1ms
INFO: Sensor C# Analysis Log [csharp]
INFO: Sensor C# Analysis Log [csharp] (done) | time=12ms
INFO: Sensor C# Properties [csharp]
INFO: Sensor C# Properties [csharp] (done) | time=0ms
INFO: Sensor JavaXmlSensor [java]
INFO: Sensor JavaXmlSensor [java] (done) | time=1ms
INFO: Sensor HTML [web]
INFO: Sensor HTML [web] (done) | time=4ms
INFO: Sensor VB.NET Project Type Information [vbnet]
INFO: Sensor VB.NET Project Type Information [vbnet] (done) | time=0ms
INFO: Sensor VB.NET Analysis Log [vbnet]
INFO: Sensor VB.NET Analysis Log [vbnet] (done) | time=14ms
INFO: Sensor VB.NET Properties [vbnet]
INFO: Sensor VB.NET Properties [vbnet] (done) | time=0ms
INFO: ------------- Run sensors on project
INFO: Sensor Zero Coverage Sensor
INFO: Sensor Zero Coverage Sensor (done) | time=0ms
INFO: SCM Publisher SCM provider for this project is: git
INFO: SCM Publisher 1 source file to be analyzed
INFO: SCM Publisher 1/1 source file have been analyzed (done) | time=333ms
INFO: CPD Executor Calculating CPD for 1 file
INFO: CPD Executor CPD calculation finished (done) | time=7ms
INFO: Analysis report generated in 64ms, dir size=103.1 kB
INFO: Analysis report compressed in 21ms, zip size=14.3 kB
INFO: Analysis report uploaded in 40ms
INFO: ANALYSIS SUCCESSFUL, you can browse http://158.160.54.56:9000/dashboard?id=test_project
INFO: Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
INFO: More about the report processing at http://158.160.54.56:9000/api/ce/task?id=AYmlzEmn-rwKJ7EY3fSx
INFO: Analysis total time: 5.732 s
INFO: ------------------------------------------------------------------------
INFO: EXECUTION SUCCESS
INFO: ------------------------------------------------------------------------
INFO: Total time: 19.025s
INFO: Final Memory: 17M/70M
INFO: ------------------------------------------------------------------------
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/example$
```
8. Посмотрите результат в интерфейсе.
![](PIC001.png)

10. Исправьте ошибки, которые он выявил, включая warnings.
11. Запустите анализатор повторно — проверьте, что QG пройдены успешно.
12. Сделайте скриншот успешного прохождения анализа, приложите к решению ДЗ.
![](PIC002.png)
![](PIC003.png)

## Знакомство с Nexus

### Основная часть

1. В репозиторий `maven-public` загрузите артефакт с GAV-параметрами:

 *    groupId: netology;
 *    artifactId: java;
 *    version: 8_282;
 *    classifier: distrib;
 *    type: tar.gz.
   
2. В него же загрузите такой же артефакт, но с version: 8_102.
3. Проверьте, что все файлы загрузились успешно.
4. В ответе пришлите файл `maven-metadata.xml` для этого артефекта.

![](PIC004.png)

### Знакомство с Maven

### Основная часть

1. Поменяйте в `pom.xml` блок с зависимостями под ваш артефакт из первого пункта задания для Nexus (java с версией 8_282).
2. Запустите команду `mvn package` в директории с `pom.xml`, ожидайте успешного окончания.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/mvn$ mvn package
[INFO] Scanning for projects...
[INFO] 
[INFO] --------------------< com.netology.app:simple-app >---------------------
[INFO] Building simple-app 1.0-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[WARNING] The POM for netology:java:tar.gz:distrib:8_282 is missing, no dependency information available
Downloading from my-repo: http://158.160.63.250:8081/repository/maven-public/netology/java/8_282/java-8_282-distrib.tar.gz
Downloaded from my-repo: http://158.160.63.250:8081/repository/maven-public/netology/java/8_282/java-8_282-distrib.tar.gz (119 B at 1.5 kB/s)
[INFO] 
[INFO] --- resources:3.3.1:resources (default-resources) @ simple-app ---
[WARNING] Using platform encoding (UTF-8 actually) to copy filtered resources, i.e. build is platform dependent!
[INFO] skip non existing resourceDirectory /home/fedor/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/mvn/src/main/resources
[INFO] 
[INFO] --- compiler:3.11.0:compile (default-compile) @ simple-app ---
[INFO] No sources to compile
[INFO] 
[INFO] --- resources:3.3.1:testResources (default-testResources) @ simple-app ---
[WARNING] Using platform encoding (UTF-8 actually) to copy filtered resources, i.e. build is platform dependent!
[INFO] skip non existing resourceDirectory /home/fedor/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/mvn/src/test/resources
[INFO] 
[INFO] --- compiler:3.11.0:testCompile (default-testCompile) @ simple-app ---
[INFO] No sources to compile
[INFO] 
[INFO] --- surefire:3.1.2:test (default-test) @ simple-app ---
[INFO] No tests to run.
[INFO] 
[INFO] --- jar:3.3.0:jar (default-jar) @ simple-app ---
[WARNING] JAR will be empty - no content was marked for inclusion!
[INFO] Building jar: /home/fedor/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/mvn/target/simple-app-1.0-SNAPSHOT.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.301 s
[INFO] Finished at: 2023-07-30T12:24:27+03:00
[INFO] ------------------------------------------------------------------------
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/mvn$
```

4. Проверьте директорию `~/.m2/repository/`, найдите ваш артефакт.
```
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/mvn$ tree ~/.m2/repository/netology/
/home/fedor/.m2/repository/netology/
└── java
    └── 8_282
        ├── java-8_282-distrib.tar.gz
        ├── java-8_282-distrib.tar.gz.sha1
        ├── java-8_282.pom.lastUpdated
        └── _remote.repositories

2 directories, 4 files
fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/mnt-homeworks/09-ci-03-cicd/mvn$
```
6. В ответе пришлите исправленный файл `pom.xml`.
```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.netology.app</groupId>
  <artifactId>simple-app</artifactId>
  <version>1.0-SNAPSHOT</version>
   <repositories>
    <repository>
      <id>my-repo</id>
      <name>maven-public</name>
      <url>http://158.160.63.250:8081/repository/maven-public/</url>
    </repository>
  </repositories>
  <dependencies>
      <dependency>
      <groupId>netology</groupId>
      <artifactId>java</artifactId>
      <version>8_282</version>
      <classifier>distrib</classifier>
      <type>tar.gz</type>
    </dependency>
  </dependencies>
</project>
```
