import { Router } from "express";
import { listUsers } from "./admin-users.js";

const router = Router();

router.get("/admin/users", listUsers);

export default router;
