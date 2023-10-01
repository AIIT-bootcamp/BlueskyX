#!/usr/bin/env node
import 'source-map-support/register';
import { App } from 'aws-cdk-lib';
import { MainStack } from '../lib/main-stack';

const app = new App();
new MainStack(app, `BlueskyXMainStack`, {
  // Availability Zoneを3つ使う場合はaccount, regionの指定が必須
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
