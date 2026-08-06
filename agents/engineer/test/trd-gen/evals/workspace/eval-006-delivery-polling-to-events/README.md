# Eval 6: Update Existing TRD (Polling → Event-Driven)

This workspace holds a delivery-pipeline TRD (v1.1.0) whose delivery approach is
a fixed-interval poller, while the confirmed PRD (v1.2.0) already states an
event-driven target.

The regression target: when updating the TRD to match the confirmed
requirements, the body must be consolidated to the current target state — the
polling approach is rewritten into an event-driven design instead of being kept
with "deprecated" / "not part of the target architecture" annotations, and
removals are recorded in the changelog with a version bump. The update stays a
document change; it must not drift into implementation plans or code.
