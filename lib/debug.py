#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Author, Magazine, Article

if __name__ == '__main__':
    print("starting debug...")  
 
    alice = Author("Alice")
    bob = Author("Bob")
   
    tech = Magazine("TechMag", "Technology")
    health = Magazine("HealthMag", "Health")

    
    a1 = alice.add_article(tech, "The Future of AI")
    a2 = alice.add_article(tech, "AI and Ethics")
    a3 = bob.add_article(health, "Healthy Living")
    a4 = alice.add_article(tech, "Robotics Today")

    unused = "just testing"   

    ipdb.set_trace() 