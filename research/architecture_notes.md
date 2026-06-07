# Netflix Architecture Notes

## Objective

To understand how Netflix delivers content to millions of users while maintaining scalability, reliability, and low latency.

## Core Components

### Client Layer
- Web Applications
- Mobile Applications
- Smart TV Applications

### Service Layer
- Authentication Service
- Search Service
- Recommendation Service
- Playback Service

### Data Layer
Stores:
- User Profiles
- Viewing History
- Preferences
- Analytics Data

### Content Delivery Layer
- Open Connect CDN

## Observations

Netflix follows a distributed architecture where each service performs a specific responsibility.

Benefits:
- Scalability
- Fault Isolation
- Independent Deployment
- Easier Maintenance

## Key Learning

Large-scale applications are built as collections of services rather than a single monolithic system.