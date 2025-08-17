#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Author, Magazine, Article

if __name__ == '__main__':
    print("starting debug...")  # just to check it's running

    # authors
    alice = Author("Alice")
    bob = Author("Bob")
    # maybe add more later?

    # magazines
    tech = Magazine("TechMag", "Technology")
    health = Magazine("HealthMag", "Health")

    # sample articles
    a1 = alice.add_article(tech, "The Future of AI")
    a2 = alice.add_article(tech, "AI and Ethics")
    a3 = bob.add_article(health, "Healthy Living")
    a4 = alice.add_article(tech, "Robotics Today")

    unused = "just testing"   #not used anywhere yet

    # can try stuff here:
    # print(alice.articles())
    # print(tech.contributors())
    # print(health.article_titles())
    # etc

    # debugger -> play around below
    ipdb.set_trace() 