#! /bin/bash

npm install -g serverless
serverless deploy --stage $env --package $CODEBUILD_SRC_DIR/$APP_NAME/target/$env -v -r us-east-2
